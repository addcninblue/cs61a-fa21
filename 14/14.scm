(define (nondecreaselist s)
  (if (null? s)
    s
    (let ((rest (nondecreaselist (cdr s))))
      (if ___________________
        (cons __________________ rest)
        (cons __________________ (cdr rest))))))


(define (nondecreaselist s)
    (if _____________________________
        _____________________________
        (let ((rest _____________________________ ))
            (if _____________________________
                (cons _____________________________ rest)
                (cons _____________________________ (cdr rest))))))

; (expect (nondecreaselist '(1 2 3 1 2 3)) ((1 2 3) (1 2 3)))

; (expect (nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
;         ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)))

