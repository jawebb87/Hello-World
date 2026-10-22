extern "c" fn puts(message: [*:0]const u8) c_int;

pub fn main() void {
    _ = puts("Hello, world!");
}
