from pathlib import Path

from dynaconf import Dynaconf

PATH_ROOT = Path(__file__).parent

settings = Dynaconf(
    environments=True,
    envvar_prefix="Alpha Get Values B3",
    settings_files=["settings.toml", ".secrets.toml"],
    includes=[f"{PATH_ROOT}/settings.toml", f"{PATH_ROOT}/.secrets.toml"],
)
