# Setup Notes

## Objective
Install and verify the following tools for the DevOps study environment:
- Git  
- Python 3.8+ and virtualenv  
- Docker Desktop (or Podman)  
- Visual Studio Code (VS Code)

---

## Quick verification commands
Run these after installing each tool to confirm installation.

```bash
git --version
python3 --version   # or python --version on Windows
python3 -m venv --help
docker --version    # or podman --version
code --version
```

---

## 1. Git

### Verify
```bash
git --version
```
Expected example:
```
git version 2.x.x
```

### Install
- macOS:
```bash
brew install git
```
- Ubuntu/Debian:
```bash
sudo apt update
sudo apt install git -y
```
- Windows:
Download and run the installer: https://git-scm.com/download/win

### Basic post-install setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

---

## 2. Python 3.8+ and virtualenv

### Verify
```bash
python3 --version
# or on Windows PowerShell
python --version
```
Should report Python 3.8 or newer.

### Install
- macOS:
```bash
brew install python
```
- Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```
- Windows:
Download and run installer from https://www.python.org/downloads/windows/

### Create and activate virtual environment
Create:
```bash
python3 -m venv devops-env
```
Activate:
- macOS / Linux:
```bash
source devops-env/bin/activate
```
- Windows PowerShell:
```powershell
.\devops-env\Scripts\Activate.ps1
```
Upgrade pip and install common tools:
```bash
pip install --upgrade pip setuptools wheel
pip install requests pytest
```
Deactivate:
```bash
deactivate
```

---

## 3. Docker Desktop (or Podman)

### Verify
```bash
docker --version
# test container
docker run --rm hello-world
```
Alternative:
```bash
podman --version
podman run --rm hello-world
```

### Install
- Docker Desktop:
  - macOS: https://docs.docker.com/desktop/mac/install/
  - Windows: https://docs.docker.com/desktop/windows/install/
  - Linux: follow the Docker Engine installation for your distribution (official docs)
- Podman:
  - macOS (Homebrew):
    ```bash
    brew install podman
    ```
  - Ubuntu/Debian:
    ```bash
    sudo apt update
    sudo apt install podman -y
    ```

### Linux user permissions (Docker)
To run Docker without sudo (Linux):
```bash
sudo usermod -aG docker $USER
# then log out/in or run:
newgrp docker
```

---

## 4. Visual Studio Code (VS Code)

### Verify
```bash
code --version
```
If `code` is not available on the command line, follow VS Code docs to add the command to PATH:
- In VS Code: open Command Palette (⇧⌘P / Ctrl+Shift+P) → "Shell Command: Install 'code' command in PATH" (macOS)
- On Windows, the installer can add `code` to PATH.

### Install
Download and install: https://code.visualstudio.com/

### Useful extensions (install from Extensions view or CLI)
- GitLens — eamodio.gitlens
- Python — ms-python.python
- Docker — ms-azuretools.vscode-docker
- YAML — redhat.vscode-yaml
- Kubernetes — ms-kubernetes-tools.vscode-kubernetes-tools
- Terraform — HashiCorp.terraform
- Remote - SSH — ms-vscode-remote.remote-ssh
- GitHub Pull Requests and Issues — GitHub.vscode-pull-request-github

Install via CLI (after `code` is available):
```bash
code --install-extension eamodio.gitlens
code --install-extension ms-python.python
code --install-extension ms-azuretools.vscode-docker
code --install-extension redhat.vscode-yaml
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
code --install-extension HashiCorp.terraform
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension GitHub.vscode-pull-request-github
```

---

## Troubleshooting & tips
- If `git`, `python3`, `docker`, or `code` commands are not found, ensure the binaries are in your PATH (restart terminal after installs).
- On macOS Apple Silicon, ensure you install compatible builds (some tools may require Rosetta or specific ARM builds).
- On Windows, prefer WSL2 for Linux tooling and Docker Desktop (WSL2 backend).
- For Docker on Linux, if you get permission denied, ensure your user is in the `docker` group and restart the session.
- If `code --install-extension` fails, open VS Code and install the extension through the Extensions view.

---

## Verification checklist (copy this to terminal)
```bash
# Git
git --version

# Python and venv
python3 --version
python3 -m venv devops-env
source devops-env/bin/activate    # or Windows activate command
which python                      # should point inside devops-env
deactivate

# Docker (or Podman)
docker --version
docker run --rm hello-world       # or podman run --rm hello-world

# VS Code
code --version
```

---
