let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <S-Tab> =BackwardsSnippet()
inoremap <C-Tab> 	
map! <S-Insert> <MiddleMouse>
noremap  h
snoremap <silent> 	 i<Right>=TriggerSnippet()
xmap 	 >gv
nmap 	 v>
noremap <NL> j
noremap  k
noremap  l
snoremap  b<BS>
nmap d :cs find d =expand("<cword>")
nmap i :cs find i ^=expand("<cfile>")
nmap f :cs find f =expand("<cfile>")
nmap e :cs find e =expand("<cword>")
nmap t :cs find t =expand("<cword>")
nmap c :cs find c =expand("<cword>")
nmap g :cs find g =expand("<cword>")
nmap s :cs find s =expand("<cword>")
map   /
vnoremap <silent> # :cakk VisualSearch('b')
snoremap % b<BS>%
snoremap ' b<BS>'
vnoremap <silent> * :cakk VisualSearch('f')
map ,mbt <Plug>TMiniBufExplorer
map ,mbu <Plug>UMiniBufExplorer
map ,mbc <Plug>CMiniBufExplorer
map ,mbe <Plug>MiniBufExplorer
nmap ,ihn :IHN
nmap ,is :IHS:A
nmap ,ih :IHS
map ,t :TMiniBufExplorer 
map <silent> , :onh
map ,tm :tabmove
map ,te :tat
map ,tn :tabnew
map ,e :e! ~/.vimrc 
nmap ,w :w!
nmap <slient><C-Right> 
nmap <slient><C-Left> 
nnoremap TT :TlistToggle
snoremap U b<BS>U
snoremap \ b<BS>\
vmap ]f :call PythonDec("function", 1)
vmap ]F :call PythonDec("function", -1)
vmap ]j :call PythonDec("class", 1)
vmap ]J :call PythonDec("class", -1)
vmap ]u :call PythonUncommentSelection()
vmap ]# :call PythonCommentSelection()
vmap ]> >
vmap ]< <
vmap ]e :PEoBm'gv``
vmap ]t :PBOBm'gv``
nmap ]f :call PythonDec("function", 1)
omap ]f :call PythonDec("function", 1)
nmap ]F :call PythonDec("function", -1)
omap ]F :call PythonDec("function", -1)
nmap ]j :call PythonDec("class", 1)
omap ]j :call PythonDec("class", 1)
nmap ]J :call PythonDec("class", -1)
omap ]J :call PythonDec("class", -1)
nmap ]u :call PythonUncommentSelection()
omap ]u :call PythonUncommentSelection()
nmap ]# :call PythonCommentSelection()
omap ]# :call PythonCommentSelection()
nmap ]> ]tV]e>
omap ]> ]tV]e>
nmap ]< ]tV]e<
omap ]< ]tV]e<
nmap ]e :PEoB
omap ]e :PEoB
nmap ]t :PBoB
omap ]t :PBoB
map ]v ]tV]e
map ]c :call PythonSelectObject("class")
map ]d :call PythonSelectObject("function")
map ]<Up> :call PythonNextLine(-1)
map ]<Down> :call PythonNextLine(1)
snoremap ^ b<BS>^
snoremap ` b<BS>`
nmap gx <Plug>NetrwBrowseX
map tp :tabprevious
map tn :tabnext
nmap wm :WMToggle
snoremap <Left> bi
snoremap <Right> a
snoremap <BS> b<BS>
snoremap <silent> <S-Tab> i<Right>=BackwardsSnippet()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
noremap <C-Right> l
noremap <C-Left> h
noremap <C-Up> k
noremap <C-Down> j
map <F5> :set number!
map <F3> :e . 
nnoremap <silent> <F12> :A
nmap <F7> :cp
nmap <F6> :cn
map <F4> :TlistToggle
map <C-Space> ?
xmap <S-Tab> <gv
nmap <S-Tab> v<
nmap <F2> :nohlsearch
map <S-Insert> <MiddleMouse>
inoremap <silent> 	 =TriggerSnippet()
imap  <Plug>SuperTabForward
imap  <Plug>SuperTabBackward
inoremap <silent> 	 =ShowAvailableSnips()
inoremap ( ()i
inoremap ) =ClosePair(')')
imap ,ihn :IHN
imap ,is :IHS:A
imap ,ih :IHS
imap : :	
inoremap < <>i
inoremap > =ClosePair('"')
inoremap [ []i
inoremap ] =ClosePair(']')
inoremap { {}i
inoremap } =ClosePair('}')
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set autoread
set background=dark
set backspace=indent,eol,start
set cinwords=if,elif,else,for,while,with,try,except,finally,def,class
set complete=.,w,b,u,t,i,k~/.vim/syntax/python3.0.vim,k~/.vim/plugins/python_pydiction.vim
set completeopt=longest,menu
set cscopequickfix=s-,c-,d-,i-,t-,e-
set noequalalways
set errorfile=/tmp/vijhhpp/36
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set fileformats=unix,dos,mac
set guifont=Monospace\ 10
set guioptions=aegimrLt
set helplang=cn
set history=500
set hlsearch
set ignorecase
set iminsert=0
set imsearch=0
set incsearch
set iskeyword=@,48-57,_,192-255,.,(
set matchtime=2
set mouse=a
set path=.,/usr/include,,,/usr/lib/python2.6,/usr/lib/python2.6/plat-linux2,/usr/lib/python2.6/lib-tk,/usr/lib/python2.6/lib-dynload,/usr/local/lib/python2.6/dist-packages,/usr/lib/python2.6/dist-packages,/usr/lib/python2.6/dist-packages/PIL,/usr/lib/python2.6/dist-packages/gst-0.10,/usr/lib/pymodules/python2.6,/usr/lib/python2.6/dist-packages/gtk-2.0,/usr/lib/pymodules/python2.6/gtk-2.0,/usr/lib/python2.6/dist-packages/wx-2.8-gtk2-unicode
set printoptions=paper:letter
set ruler
set runtimepath=~/.vim,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim72,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after
set shiftwidth=4
set showcmd
set smartcase
set smartindent
set smarttab
set softtabstop=4
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{CurDir()}%h\ \ \ Line:\ %l/%L:%c
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set switchbuf=useopen
set tabstop=4
set tags=./tags,./TAGS,tags,TAGS,~/.vim/tags/python.ctags
set termencoding=utf-8
set textwidth=500
set wildmenu
set window=45
set nowritebackup
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/pythonbs/system1
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +46 run.py
badd +96 serverTree.py
badd +90 config.py
badd +8 portscan.py
badd +16 terminal.py
badd +23 ssh.py
args run.py
edit run.py
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe '1resize ' . ((&lines * 1 + 23) / 46)
exe '2resize ' . ((&lines * 42 + 23) / 46)
argglobal
enew
file -MiniBufExplorer-
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> 	 :call search('\[[0-9]*:[^\]]*\]'):<BS>
nnoremap <buffer> j gj
nnoremap <buffer> k gk
nnoremap <buffer> p :wincmd p:<BS>
nnoremap <buffer> <S-Tab> :call search('\[[0-9]*:[^\]]*\]','b'):<BS>
nnoremap <buffer> <Up> gk
nnoremap <buffer> <Down> gj
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=delete
setlocal nobuflisted
setlocal buftype=nofile
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,elif,else,for,while,with,try,except,finally,def,class
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i,k~/.vim/syntax/python3.0.vim,k~/.vim/plugins/python_pydiction.vim
setlocal completefunc=
setlocal nocopyindent
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != ''
setlocal filetype=
endif
setlocal foldcolumn=0
setlocal foldenable
set foldexpr=PythonFoldExpr(v:lnum)
setlocal foldexpr=PythonFoldExpr(v:lnum)
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
set foldmethod=expr
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
set foldtext=PythonFoldText()
setlocal foldtext=PythonFoldText()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255,.,(
setlocal keywordprg=
set linebreak
setlocal linebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal nomodifiable
setlocal nrformats=octal,hex
set number
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != ''
setlocal syntax=
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=500
setlocal thesaurus=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
wincmd w
argglobal
noremap <buffer> <silent>  :PyflakesUpdate
map <buffer> ,pK :call ShowPyDoc('', 0)
map <buffer> ,pk :call ShowPyDoc('', 0)
map <buffer> ,pW :call ShowPyDoc('', 1)
map <buffer> ,pw :call ShowPyDoc('', 1)
map <buffer> E :w:!/usr/bin/env python % 
map <buffer> F :call ToggleFold()
nnoremap <buffer> <silent> K :call ShowPyDoc(expand("<cword>"), 1)
noremap <buffer> <silent> dw dw:PyflakesUpdate
noremap <buffer> <silent> dd dd:PyflakesUpdate
map <buffer> f za
map <buffer> gd /def  
noremap <buffer> <silent> u u:PyflakesUpdate
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal balloonexpr=
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,elif,else,for,while,with,try,except,finally,def,class
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i,k~/.vim/syntax/python3.0.vim,k~/.vim/plugins/python_pydiction.vim
setlocal completefunc=
setlocal nocopyindent
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal foldcolumn=0
setlocal foldenable
set foldexpr=PythonFoldExpr(v:lnum)
setlocal foldexpr=GetPythonFold(v:lnum)
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
set foldmethod=expr
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
set foldtext=PythonFoldText()
setlocal foldtext=PythonFoldText()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=
setlocal includeexpr=
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255,.,(
setlocal keywordprg=
set linebreak
setlocal linebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=500
setlocal thesaurus=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
31
normal zo
37
normal zo
146
normal zc
31
normal zo
271
normal zo
271
normal zc
295
normal zc
309
normal zc
271
normal zo
let s:l = 47 - ((1 * winheight(0) + 21) / 42)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
47
normal! 016l
wincmd w
2wincmd w
exe '1resize ' . ((&lines * 1 + 23) / 46)
exe '2resize ' . ((&lines * 42 + 23) / 46)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
