from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    USERNAME_FG = 52
    USERNAME_BG = 223
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 52
    HOSTNAME_BG = 186

    HOME_SPECIAL_DISPLAY = False
    PATH_FG = 52
    PATH_BG = 151
    CWD_FG = 16
    SEPARATOR_FG = 23

    READONLY_BG = 1
    READONLY_FG = 7

    REPO_CLEAN_FG = 14
    REPO_CLEAN_BG = 0
    REPO_DIRTY_FG = 3
    REPO_DIRTY_BG = 0

    JOBS_FG = 4
    JOBS_BG = 8

    CMD_PASSED_FG = 15
    CMD_PASSED_BG = 2
    CMD_FAILED_FG = 15
    CMD_FAILED_BG = 1

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    VIRTUAL_ENV_BG = 15
    VIRTUAL_ENV_FG = 2

    AWS_PROFILE_FG = 7
    AWS_PROFILE_BG = 2

    TIME_FG = 15
    TIME_BG = 10
