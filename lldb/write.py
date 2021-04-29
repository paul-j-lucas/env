from __future__ import print_function
import argparse
import lldb
import re

###############################################################################

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f write.write_impl write')


def parse_args(raw_args):
    """Parse the arguments given to write."""
    parser = argparse.ArgumentParser(
        # Need to provide 'prog' (name of program) here otherwise argparse
        # tries to get it from sys.argv[0], which breaks when called in lldb.
        prog='write',
        description='Write the output of an lldb command to file.'
    )

    parser.add_argument('filename')
    parser.add_argument('command', nargs='+')
    args = parser.parse_args(raw_args.split(' '))

    # The parser splits the command into a list, e.g., ['register', 'read'].
    # Convert it back to a string so we can later pass it to lldb for
    # evaluation.
    args.command = ' '.join(args.command)

    return args


def strip_esc_seq(s):
    """Strip ANSI escape sequences from string."""
    esc_seq_re = re.compile(r'\x1b[^m]*m')
    return esc_seq_re.sub('', s)


def write_impl(debugger, raw_args, result, internal_dict):
    """Recceives and handles the call to write from lldb."""
    args = parse_args(raw_args)

    # Run the command and store the result.
    rv = lldb.SBCommandReturnObject()
    interpreter = lldb.debugger.GetCommandInterpreter()
    interpreter.HandleCommand(args.command, rv)

    # Write to file.
    output = rv.GetOutput() or rv.GetError()
    f = open(args.filename, 'w')
    f.write("(lldb) " + args.command + '\n\n')
    f.write(strip_esc_seq(output))
    f.close()


###############################################################################
# vim:set et sw=4 ts=4:
