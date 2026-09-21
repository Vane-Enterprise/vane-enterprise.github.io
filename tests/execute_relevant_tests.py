# Intelligent test execution strategy
Implement smart test execution that runs only relevant tests based on changed code:

```Bash
#!/usr/bin/env bash
# Intelligent test execution based on change impact

execute_relevant_tests() {
    local changed_files=$(git diff --cached --name-only)
    local test_failures=0

    echo "Analyzing test requirements for changed files..."

    # Check if source code changes require testing
    if echo "$changed_files" | grep -qE "\.(js|jsx|ts|tsx|py|cs|go)$"; then
        echo "Source code changes detected, running relevant tests..."

        # JavaScript/TypeScript projects
        if [ -f "package.json" ] && command -v npm >/dev/null 2>&1; then
            if echo "$changed_files" | grep -qE "\.(js|jsx|ts|tsx)$"; then
                echo "Running JavaScript/TypeScript tests..."
                npm test -- --findRelatedTests $changed_files --passWithNoTests || ((test_failures++))
            fi
        fi

        # Python projects
        if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
            if echo "$changed_files" | grep -qE "\.py$"; then
                echo "Running Python tests..."
                if command -v pytest >/dev/null 2>&1; then
                    pytest --tb=short || ((test_failures++))
                elif command -v python3 >/dev/null 2>&1; then
                    python3 -m unittest discover || ((test_failures++))
                fi
            fi
        fi

        # .NET projects
        if find . -name "*.csproj" -o -name "*.sln" | grep -q .; then
            if echo "$changed_files" | grep -qE "\.cs$"; then
                echo "Running .NET tests..."
                dotnet test --no-build --verbosity minimal || ((test_failures++))
            fi
        fi

        # Go projects
        if [ -f "go.mod" ]; then
            if echo "$changed_files" | grep -qE "\.go$"; then
                echo "Running Go tests..."
                go test ./... || ((test_failures++))
            fi
        fi
    fi

    if [ $test_failures -gt 0 ]; then
        echo "Test execution failed"
        echo "Please fix failing tests before committing"
        return 1
    fi

    echo "All relevant tests passed"
    return 0
}

# Execute intelligent testing
execute_relevant_tests || exit 1
