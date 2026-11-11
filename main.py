if __package__:
  from .utils import ensure_directories, main_menu
else:
  from utils import ensure_directories, main_menu


if __name__ == "__main__":
  ensure_directories()
  main_menu()