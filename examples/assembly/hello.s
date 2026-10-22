.section .rodata
message:
    .ascii "Hello, world!\n"
.set message_length, . - message

.section .text
.global _start
_start:
    mov $1, %rax
    mov $1, %rdi
    lea message(%rip), %rsi
    mov $message_length, %rdx
    syscall

    mov $60, %rax
    xor %rdi, %rdi
    syscall

.section .note.GNU-stack,"",@progbits
