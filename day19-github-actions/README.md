# Day 19 - GitHub Actions & CI Automation

## Objective
Learn GitHub Actions, workflow triggers, automated validation,
CI execution, failure diagnosis, and recovery.

## Concepts
- Workflow: automated process defined in YAML.
- Job: group of tasks executed by a runner.
- Step: individual action or command.
- Runner: machine that executes workflow jobs.
- Trigger: event that starts a workflow.
- CI: automated validation of code changes.

## Workflow
Repository Push / Pull Request
        |
        v
GitHub Actions Trigger
        |
        v
Ubuntu Runner
        |
        v
Checkout Repository
        |
        v
File Existence Checks
        |
        v
Bash Syntax Validation
        |
        v
CI Result

## Automated Checks
- Verify Day 19 README exists.
- Verify Day 18 health-check script exists.
- Validate Bash script syntax using bash -n.
- Print success message when all checks pass.

## Failure & Recovery Exercise
1. Changed README validation to a nonexistent file.
2. Pushed the faulty workflow configuration.
3. Observed the CI failure in GitHub Actions.
4. Identified the incorrect file path.
5. Restored the correct README path.
6. Committed and pushed the fix.
7. Verified local file validation.

## Key Commands
- `git push origin main` - triggers the push workflow.
- `test -f FILE` - verifies that a file exists.
- `bash -n FILE` - validates Bash syntax without executing the script.
- `git diff --check` - checks patch whitespace errors.
- `git status` - checks repository state.

## Outcome
Built a GitHub Actions workflow with push and pull request triggers,
automated repository checks, and practiced CI troubleshooting
through an intentional failure and recovery.

## Skills Practiced
GitHub Actions, YAML, CI, automated testing,
Linux shell, debugging, failure analysis, Git and GitHub.
