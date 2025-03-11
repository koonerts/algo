# Algo Repository Guidelines

## Build Commands

### C++ (cpp-algo)
- Build: `mkdir build && cd build && conan install .. && cmake .. && make`
- Run: `./cpp_algo` (from build directory)
- Test: `./tests` (all tests) or `./tests "[test-name]"` (specific test)

### Go (go-algo)
- Build: `go build && ./go-algo`
- Run: `go run main.go`
- Test: `go test ./...` (all) or `go test ./arr -run TestFunctionName` (specific)
- Format: `gofmt -w .`

### Python (py-algo)
- Setup: `poetry install`
- Run: `poetry run python <script_path>`
- Environment: Uses Python 3.9+

### C# (csharp-algo)
- Build: `dotnet build csharp-algo/csharp-algo.sln`
- Run: `dotnet run --project csharp-algo/csharp-algo/csharp-algo.csproj`
- Target: .NET 5.0

### Hack (hack-algo)
- Setup: `composer install`
- Run: `hhvm src/main.hack`
- Lint: `vendor/bin/hhast-lint`

## Code Style Conventions

- **Naming**: 
  - Types/Classes: PascalCase (MinHeap, ListNode)
  - Functions/Methods: camelCase (addItem, findPath)
  - Private fields: _prefixed (_heap, _count)
  - Constants: UPPER_SNAKE_CASE (MAX_SIZE)
- **Types**: Use explicit type annotations (Go interfaces, C++ templates, TypeScript types)
- **Documentation**: Functions should have descriptive docstrings with examples
- **Testing**: Use table-driven tests with clear input/expected pairs
- **Error Handling**: Check errors immediately and return early
- **Formatting**: 4-space indentation, language-specific brace style
- **Organization**: Code arranged by topic/domain (arrays, trees, graphs)