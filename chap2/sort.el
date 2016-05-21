(require 'cl)

(defun exch (a x y)
  (let ((tmp (nth x a)))
    (setf (nth x a) (nth y a) (nth y a) tmp)
    a))

(defun selection-sort (xs)
  (selection-sort-tailrec xs nil))

(defun selection-sort-tailrec (xs sorted-xs)
  (loop for i from 0 to (- (length xs) 1) collect
        (when (> (nth 0 xs) (nth i xs))
          (exch xs 0 i)
          (first xs))))
               
(selection-sort (cl-loop for i from 0 to 9
                         collect (random 100)))
