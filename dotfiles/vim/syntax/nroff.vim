syn clear

syn region nroffIgnore  start=/^[.']\s*ig/ end=/^['.]\s*\./
syn match  nroffCommand "^\.[a-zA-Z][a-zA-Z0-9]*"
syn match  nroffCommand "^\.\."
syn match  nroffComment /^\.\\".*/
syn match  nroffFont    "\\f\([A-Z1-9]\|([A-Z1-9]\{2}\)"
syn match  nroffSize    "\\s[0-9]*"

hi      nroffIgnore   cterm=NONE ctermfg=DarkBlue ctermbg=NONE
hi link nroffCommand  PreProc
hi link nroffComment  Comment
hi      nroffFont     cterm=NONE ctermfg=Cyan ctermbg=NONE
hi      nroffSize     cterm=NONE ctermfg=Cyan ctermbg=NONE

let b:current_syntax = "nroff"

" vim:set et sw=2 ts=2:
