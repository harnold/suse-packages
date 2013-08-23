(autoload 'caml-mode "caml" "Major mode for editing OCaml code." t)
(autoload 'run-caml "inf-caml" "Run an inferior OCaml process." t)
(autoload 'camldebug "camldebug" "Run ocamldebug on program." t)

(push '("\\.ml[iylp]?$" . caml-mode) auto-mode-alist)
(push '("ocamlrun" . caml-mode) interpreter-mode-alist)
(push '("ocaml" . caml-mode) interpreter-mode-alist)
