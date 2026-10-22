# Hello, world! in every language

An expanding collection of tiny programs that print:

```text
Hello, world!
```

Currently includes 65 programming languages. This is not an exhaustive list; new languages are welcome.

## Run an example

Install the language's compiler or interpreter, change into its directory, and run the command below. Commands assume a Unix-like shell; compiled examples create local build artifacts.

For example:

```sh
cd examples/python
python3 hello.py
```

## Languages

| Language | Source | Run from the source directory |
| --- | --- | --- |
| Ada | [hello.adb](examples/ada/hello.adb) | `gnatmake hello.adb && ./hello` |
| AppleScript | [hello.applescript](examples/applescript/hello.applescript) | `osascript hello.applescript` |
| Assembly (x86-64) | [hello.s](examples/assembly/hello.s) | `as --64 hello.s -o hello.o && ld hello.o -o hello && ./hello` |
| AWK | [hello.awk](examples/awk/hello.awk) | `awk -f hello.awk` |
| Bash | [hello.sh](examples/bash/hello.sh) | `bash hello.sh` |
| bc | [hello.bc](examples/bc/hello.bc) | `bc -q hello.bc` |
| Befunge-93 | [hello.bf](examples/befunge/hello.bf) | `bef -q hello.bf` |
| Brainfuck | [hello.bf](examples/brainfuck/hello.bf) | `beef hello.bf` |
| C | [hello.c](examples/c/hello.c) | `cc hello.c -o hello && ./hello` |
| C# | [hello.cs](examples/csharp/hello.cs) | `csc hello.cs && mono hello.exe` |
| C++ | [hello.cpp](examples/cpp/hello.cpp) | `c++ hello.cpp -o hello && ./hello` |
| Clojure | [hello.clj](examples/clojure/hello.clj) | `clojure hello.clj` |
| COBOL | [hello.cob](examples/cobol/hello.cob) | `cobc -x -free hello.cob -o hello && ./hello` |
| CoffeeScript | [hello.coffee](examples/coffeescript/hello.coffee) | `coffee hello.coffee` |
| Common Lisp | [hello.lisp](examples/common-lisp/hello.lisp) | `sbcl --script hello.lisp` |
| Crystal | [hello.cr](examples/crystal/hello.cr) | `crystal run hello.cr` |
| D | [hello.d](examples/d/hello.d) | `dmd hello.d -of=hello && ./hello` |
| Dart | [hello.dart](examples/dart/hello.dart) | `dart run hello.dart` |
| Elixir | [hello.exs](examples/elixir/hello.exs) | `elixir hello.exs` |
| Erlang | [hello.erl](examples/erlang/hello.erl) | `erlc hello.erl && erl -noshell -s hello main -s init stop` |
| F# | [hello.fsx](examples/fsharp/hello.fsx) | `dotnet fsi hello.fsx` |
| Fish | [hello.fish](examples/fish/hello.fish) | `fish hello.fish` |
| Forth | [hello.fs](examples/forth/hello.fs) | `gforth hello.fs -e bye` |
| Fortran | [hello.f90](examples/fortran/hello.f90) | `gfortran hello.f90 -o hello && ./hello` |
| FreeBASIC | [hello.bas](examples/freebasic/hello.bas) | `fbc hello.bas -x hello && ./hello` |
| Go | [hello.go](examples/go/hello.go) | `go run hello.go` |
| Groovy | [hello.groovy](examples/groovy/hello.groovy) | `groovy hello.groovy` |
| Haskell | [hello.hs](examples/haskell/hello.hs) | `runghc hello.hs` |
| Java | [Hello.java](examples/java/Hello.java) | `javac Hello.java && java Hello` |
| JavaScript | [hello.js](examples/javascript/hello.js) | `node hello.js` |
| Julia | [hello.jl](examples/julia/hello.jl) | `julia hello.jl` |
| Kotlin | [hello.kts](examples/kotlin/hello.kts) | `kotlinc -script hello.kts` |
| LOLCODE | [hello.lol](examples/lolcode/hello.lol) | `lci hello.lol` |
| Lua | [hello.lua](examples/lua/hello.lua) | `lua hello.lua` |
| M4 | [hello.m4](examples/m4/hello.m4) | `m4 hello.m4` |
| Nim | [hello.nim](examples/nim/hello.nim) | `nim compile --run hello.nim` |
| Objective-C | [hello.m](examples/objective-c/hello.m) | `clang -framework Foundation hello.m -o hello && ./hello` |
| OCaml | [hello.ml](examples/ocaml/hello.ml) | `ocaml hello.ml` |
| Octave | [hello.m](examples/octave/hello.m) | `octave --quiet --no-gui hello.m` |
| Ook! | [hello.ook](examples/ook/hello.ook) | `python3 ../../tools/ook_to_brainfuck.py hello.ook > hello.bf && beef hello.bf` |
| Pascal | [hello.pas](examples/pascal/hello.pas) | `fpc hello.pas && ./hello` |
| Perl | [hello.pl](examples/perl/hello.pl) | `perl hello.pl` |
| PHP | [hello.php](examples/php/hello.php) | `php hello.php` |
| PostScript | [hello.ps](examples/postscript/hello.ps) | `gs -q -dNODISPLAY -dBATCH hello.ps` |
| PowerShell | [hello.ps1](examples/powershell/hello.ps1) | `pwsh -File hello.ps1` |
| Prolog | [hello.pl](examples/prolog/hello.pl) | `swipl -q -s hello.pl` |
| Python | [hello.py](examples/python/hello.py) | `python3 hello.py` |
| R | [hello.R](examples/r/hello.R) | `Rscript hello.R` |
| Racket | [hello.rkt](examples/racket/hello.rkt) | `racket hello.rkt` |
| Raku | [hello.raku](examples/raku/hello.raku) | `raku hello.raku` |
| Ruby | [hello.rb](examples/ruby/hello.rb) | `ruby hello.rb` |
| Rust | [hello.rs](examples/rust/hello.rs) | `rustc hello.rs -o hello && ./hello` |
| Scala | [hello.scala](examples/scala/hello.scala) | `scalac hello.scala && scala Hello` |
| Scheme | [hello.scm](examples/scheme/hello.scm) | `guile -s hello.scm` |
| Smalltalk | [hello.st](examples/smalltalk/hello.st) | `gst -q hello.st` |
| SQL | [hello.sql](examples/sql/hello.sql) | `sqlite3 -batch -noheader :memory: < hello.sql` |
| Standard ML | [hello.sml](examples/standard-ml/hello.sml) | `mlton -output hello hello.sml && ./hello` |
| Swift | [hello.swift](examples/swift/hello.swift) | `swift hello.swift` |
| Tcl | [hello.tcl](examples/tcl/hello.tcl) | `tclsh hello.tcl` |
| TypeScript | [hello.ts](examples/typescript/hello.ts) | `tsc hello.ts && node hello.js` |
| Vala | [hello.vala](examples/vala/hello.vala) | `valac hello.vala -o hello && ./hello` |
| Verilog | [hello.v](examples/verilog/hello.v) | `iverilog -o hello hello.v && vvp hello` |
| Visual Basic | [Hello.vb](examples/visual-basic/Hello.vb) | `vbnc Hello.vb && mono Hello.exe` |
| Whitespace | [hello.ws](examples/whitespace/hello.ws) | `whitepycli hello.ws` |
| Zig | [hello.zig](examples/zig/hello.zig) | `zig run hello.zig -lc` |

C# and Visual Basic examples use Mono (`csc` and `vbnc` respectively). Scheme uses GNU Guile, Common Lisp uses SBCL, and Prolog uses SWI-Prolog. Toolchains are installed separately; the repository has no shared runtime dependencies.

## Runtime notes

- AppleScript requires macOS. The Objective-C command also targets macOS and requires Apple's command-line developer tools and Foundation framework.
- Assembly uses GNU assembler syntax and Linux x86-64 system calls; it requires GNU Binutils on Linux x86-64.
- bc uses the GNU bc `print` extension. See the [GNU bc statement reference](https://www.gnu.org/software/bc/manual/html_chapter/bc_4.html).
- COBOL uses GnuCOBOL with free-format source. See the [GnuCOBOL manual](https://gnucobol.sourceforge.io/doc/gnucobol.html).
- CoffeeScript requires its `coffee` CLI and Node.js. See the [CoffeeScript documentation](https://coffeescript.org/).
- Forth uses Gforth; `-e bye` exits after running the file. See [invoking Gforth](https://gforth.org/manual/Invoking-Gforth.html).
- FreeBASIC uses `fbc`; Standard ML uses MLton; Smalltalk uses GNU Smalltalk; Raku uses Rakudo.
- Octave uses GNU Octave. PostScript uses Ghostscript in console mode.
- SQL uses the SQLite CLI with an in-memory database and no column headers.
- Vala requires its compiler, a C compiler, and GLib development files.
- Verilog uses the Icarus Verilog compiler and simulator. See the [Icarus getting-started guide](https://github.com/steveicarus/iverilog/blob/master/Documentation/usage/getting_started.rst).
- Zig links libc with `-lc` and calls `puts` to write to standard output.

## Esoteric languages

These five examples also print exactly `Hello, world!` and a newline.

| Language | What makes it unusual | Interpreter / reference |
| --- | --- | --- |
| Brainfuck | Eight instructions operate on a tape of memory cells. | [Beef interpreter](https://github.com/andreabolognani/beef) |
| Befunge-93 | Instructions occupy a two-dimensional grid. This example pushes a reversed string, then pops characters to print it. | [Reference interpreter and specification](https://github.com/catseye/Befunge-93) |
| LOLCODE | Keywords resemble internet cat captions: `HAI`, `VISIBLE`, and `KTHXBYE`. | [lci interpreter](https://github.com/justinmeza/lci) |
| Ook! | Each Brainfuck instruction becomes a pair of `Ook.`, `Ook?`, or `Ook!` tokens. | [Language creator's specification](https://www.dangermouse.net/esoteric/ook.html) |
| Whitespace | Only spaces, tabs, and line feeds carry instructions. | [whitepy interpreter and usage](https://github.com/yasn77/whitepy) |

Install the linked interpreter separately. Befunge uses the reference interpreter's `-q` option to suppress its banner. Whitespace's command is `whitepycli`, provided by the `whitepy` Python package.

Ook! uses the included [converter](tools/ook_to_brainfuck.py), followed by Beef. The generated `examples/ook/hello.bf` is ignored by Git. The converter requires only Python 3 and rejects malformed tokens and unmatched loops.

The Whitespace file looks empty in most editors. Do not trim its spaces, replace tabs, or normalize its final newlines. The repository's EditorConfig and Git attributes preserve those bytes in tools that honor them. To inspect the source from the repository root:

```sh
python3 -c 'from pathlib import Path; print(repr(Path("examples/whitespace/hello.ws").read_bytes()))'
```

Run the Ook! converter checks from the repository root:

```sh
python3 -m unittest discover -s tests
```

## Add a language

1. Create `examples/<language>/` using a lowercase directory name.
2. Add the smallest readable program that prints exactly `Hello, world!` followed by a newline.
3. Add its source link and run command to the alphabetical table above.
4. Run it with its compiler or interpreter and check the output. Note any special runtime requirements.

Keep each example self-contained and omit generated binaries from commits.
