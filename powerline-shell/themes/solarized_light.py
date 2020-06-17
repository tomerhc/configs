from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    USERNAME_FG = 237
    USERNAME_BG = 110
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 237
    HOSTNAME_BG = 31

    HOME_SPECIAL_DISPLAY = False
    PATH_FG = 237
    PATH_BG = 117
    CWD_FG = 232
    SEPARATOR_FG = 31

    READONLY_BG = 1
    READONLY_FG = 7

    REPO_CLEAN_FG = 0
    REPO_CLEAN_BG = 15
    REPO_DIRTY_FG = 1
    REPO_DIRTY_BG = 15

    JOBS_FG = 4
    JOBS_BG = 7

    CMD_PASSED_FG = 15
    CMD_PASSED_BG = 2
    CMD_FAILED_FG = 15
    CMD_FAILED_BG = 1

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    VIRTUAL_ENV_BG = 15
    VIRTUAL_ENV_FG = 2

    TIME_FG = 15
    TIME_BG = 10
