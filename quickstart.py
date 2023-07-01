from pathlib import Path

import github_secret_syncer

base_dir = Path(__file__).parent

github_secret_syncer.sync_secrets(
    dotenv_path=base_dir / ".env",
    owner="your_github_username",
    repo="your_github_repo_name",
    github_pat="your_github_personal_access_token",
)
