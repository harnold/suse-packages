;;; Emacs loads this file before "~/.emacs" and "default.el"

(let* ((site-lisp-dir "/usr/share/emacs/site-lisp")
       (site-start-dir (concat site-lisp-dir "/site-start.d"))
       (site-start-files
        (append
         (if (file-accessible-directory-p site-start-dir)
             (directory-files site-start-dir t "\\.elc?\\'"))
         (directory-files site-lisp-dir t "^suse-start-.*\\.elc?$"))))
  (mapc 'load
        (delete-dups
         (mapcar 'file-name-sans-extension
                 site-start-files))))
