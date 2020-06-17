set nocompatible              " required
filetype off                  " required


" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

" ...

set rnu
Plugin 'rust-lang/rust.vim'




call vundle#end()            " required
filetype plugin indent on    " required


let g:lightline = { 'colorscheme': 'plastic' }
let @p='aprintln!("{}", );bbllli'


set background=dark
syntax on

