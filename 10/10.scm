; (define (fib n)
;   (if (<= n 1)
;     n
;     (+ (fib (- n 1)) (fib (- n 2)))))

(define (fib n)
  (define (fib-helper n curr prev)
    (if (= n 0)
      curr
      (fib-helper (- n 1) (+ curr prev) curr)))
  (fib-helper n 0 1))

; (define with-list
;   (list ... ))

; (define with-quote
;   '(...))

; (define helpful-list
;    (cons 'a (cons 'b nil)))

; (define another-helpful-list
;     (cons 'c (cons 'd (cons (cons 'e nil) nil))))

; (define with-cons
;     (cons helpful-list another-helpful-list))


(define (list-concat a b)
  (if (null? a)
    b
    (cons (car a) (list-concat (cdr a) b))))

(define (map-fn fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map-fn fn (cdr lst)))))

(define (make-tree label branches) (cons label branches))

(define (label tree) (car tree))

(define (branches tree) (cdr tree))

(define (tree-sum tree)
  (+ ))
