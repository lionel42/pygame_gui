import pytest

from pygame_gui.core import BlockingThreadedResourceLoader
from pygame_gui.core.ui_font_dictionary import UIFontDictionary


class TestUIFontDictionary:
    def test_creation(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        assert font_dictionary.loaded_fonts is not None

    def test_load_default_font_from_strings(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        font_dictionary._load_default_font()
        font_dictionary.preload_font(font_size=14, font_name='fira_code', bold=True)
        font_dictionary.preload_font(font_size=14, font_name='fira_code', italic=True)
        font_dictionary.preload_font(font_size=14, font_name='fira_code', bold=True, italic=True)

        assert font_dictionary.loaded_fonts is not None

    def test_find_font_unloaded_size(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')

        with pytest.warns(UserWarning, match="Finding font with id"):
            font_dictionary.find_font(font_size=20, font_name='fira_code')

    def test_find_font_unloaded_style_bold(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')

        with pytest.warns(UserWarning, match="Finding font with id"):
            font_dictionary.find_font(font_size=20, font_name='fira_code', bold=True)

    def test_find_font_unloaded_style_italic(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')

        with pytest.warns(UserWarning, match="Finding font with id"):
            font_dictionary.find_font(font_size=20, font_name='fira_code', italic=True)

    def test_find_font_unloaded_style_bold_italic(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')

        with pytest.warns(UserWarning, match="Finding font with id"):
            font_dictionary.find_font(font_size=20, font_name='fira_code', bold=True, italic=True)

    def test_find_font_unloaded(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')

        font_dictionary.find_font(font_size=20, font_name='arial')

    def test_create_font_id(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        font_id_1 = font_dictionary.create_font_id(font_size=10, font_name='bob', bold=False, italic=False)
        assert font_id_1 == 'bob_regular_10'

        font_id_1 = font_dictionary.create_font_id(font_size=10, font_name='bob', bold=True, italic=False)
        assert font_id_1 == 'bob_bold_10'

        font_id_1 = font_dictionary.create_font_id(font_size=10, font_name='bob', bold=False, italic=True)
        assert font_id_1 == 'bob_italic_10'

        font_id_1 = font_dictionary.create_font_id(font_size=10, font_name='bob', bold=True, italic=True)
        assert font_id_1 == 'bob_bold_italic_10'

        with pytest.warns(UserWarning, match="Font size less than or equal to 0"):
            font_dictionary.create_font_id(font_size=-50, font_name='bob', bold=True, italic=True)

    def test_preload_already_loaded(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        with pytest.warns(UserWarning, match="Trying to pre-load font id"):
            font_dictionary.preload_font(font_name='fira_code', font_size=14)

    def test_preload_no_paths(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        with pytest.warns(UserWarning, match="Trying to pre-load font id"):
            font_dictionary.preload_font(font_name='arial', font_size=14)

    def test_preload_bad_paths(self, _init_pygame):
        loader = BlockingThreadedResourceLoader()
        font_dictionary = UIFontDictionary(loader, locale='en')
        loader.start()
        loader.update()
        font_dictionary.add_font_path('arial',
                                      font_path='doop/doop/doop.ttf',
                                      bold_path='doop/doop/doop.ttf',
                                      italic_path='doop/doop/doop.ttf',
                                      bold_italic_path='doop/doop/doop.ttf'
                                      )
        with pytest.warns(UserWarning, match="Unable to load resource with path"):
            font_dictionary.preload_font(font_name='arial', font_size=14)

        with pytest.warns(UserWarning, match="Unable to load resource with path"):
            font_dictionary.preload_font(font_name='arial', font_size=14, bold=True)

        with pytest.warns(UserWarning, match="Unable to load resource with path"):
            font_dictionary.preload_font(font_name='arial', font_size=14, italic=True)

        with pytest.warns(UserWarning, match="Unable to load resource with path"):
            font_dictionary.preload_font(font_name='arial', font_size=14, bold=True, italic=True)

    def test_add_font_path(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        font_dictionary.add_font_path('arial',
                                      font_path='doop/doop/doop.ttf',
                                      bold_path='doop/doop/doop.ttf',
                                      italic_path='doop/doop/doop.ttf',
                                      bold_italic_path='doop/doop/doop.ttf'
                                      )

        assert 'arial' in font_dictionary.known_font_paths

    def test_print_unused_loaded_fonts(self, _init_pygame, capsys):
        loader = BlockingThreadedResourceLoader()
        font_dictionary = UIFontDictionary(loader, locale='en')
        font_dictionary.add_font_path(font_name='roboto',
                                      font_path='tests/data/Roboto-Regular.ttf')
        font_dictionary.preload_font(font_name='roboto', font_size=14)

        loader.start()
        loader.update()

        font_dictionary.print_unused_loaded_fonts()
        captured = capsys.readouterr()

        assert captured.out == 'Unused font ids:\nroboto_regular_14(HTML size: 4)\n'

    def test_convert_html_size_to_point_size_invalid(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        assert font_dictionary.convert_html_to_point_size(9000) == font_dictionary.default_font.size

    def test_convert_html_size_to_point_size_valid(self, _init_pygame):
        font_dictionary = UIFontDictionary(BlockingThreadedResourceLoader(), locale='en')
        assert font_dictionary.convert_html_to_point_size(3) == 12

    def test_check_font_preloaded(self, _init_pygame):
        loader = BlockingThreadedResourceLoader()

        font_dictionary = UIFontDictionary(loader, locale='en')
        font_dictionary.add_font_path(font_name='roboto',
                                      font_path='tests/data/Roboto-Regular.ttf')
        font_dictionary.preload_font(font_name='roboto', font_size=14)

        loader.start()
        loader.update()

        assert font_dictionary.check_font_preloaded('roboto_regular_14')


if __name__ == '__main__':
    pytest.console_main()
