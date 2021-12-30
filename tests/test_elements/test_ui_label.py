import os
import pytest
import pygame

from tests.shared_comparators import compare_surfaces

from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_label import UILabel
from pygame_gui.core.ui_container import UIContainer


class TestUILabel:

    def test_creation(self, _init_pygame, default_ui_manager,
                      _display_surface_return_none):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager)
        assert label.image is not None

    def test_set_text(self, _init_pygame, default_ui_manager,
                      _display_surface_return_none):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager)
        label.set_text("new text")
        assert label.image is not None

    def test_rebuild(self, _init_pygame, default_ui_manager,
                     _display_surface_return_none):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager)
        label.rebuild()
        assert label.image is not None

    def test_rebuild_from_theme_data_non_default_1(self, _init_pygame):
        manager = UIManager((800, 600), os.path.join("tests", "data", "themes",
                                                     "ui_label_non_default_1.json"))
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=manager)
        assert label.image is not None

    def test_rebuild_from_theme_data_non_default_2(self, _init_pygame):
        manager = UIManager((800, 600), os.path.join("tests", "data", "themes",
                                                     "ui_label_non_default_2.json"))
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=manager)
        assert label.image is not None

    def test_rebuild_from_theme_data_non_default_3(self, _init_pygame):
        manager = UIManager((800, 600), os.path.join("tests", "data", "themes",
                                                     "ui_label_non_default_3.json"))
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=manager)
        assert label.image is not None

    @pytest.mark.filterwarnings("ignore:Invalid value")
    @pytest.mark.filterwarnings("ignore:Colour hex code")
    @pytest.mark.filterwarnings("ignore:Label Rect is too small for text")
    def test_rebuild_from_theme_data_bad_values(self, _init_pygame):
        manager = UIManager((800, 600), os.path.join("tests", "data", "themes",
                                                     "ui_label_bad_values.json"))
        label = UILabel(relative_rect=pygame.Rect(100, 100, 10, 30),
                        text="Test Label",
                        manager=manager)
        assert label.image is not None

    def test_set_position(self, _init_pygame, default_ui_manager,
                          _display_surface_return_none):
        test_container = UIContainer(relative_rect=pygame.Rect(100, 100, 300, 60),
                                     manager=default_ui_manager)
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        container=test_container,
                        manager=default_ui_manager)

        label.set_position(pygame.math.Vector2(150.0, 30.0))

        assert label.relative_rect.topleft == (50, -70)

    def test_set_relative_position(self, _init_pygame, default_ui_manager,
                                   _display_surface_return_none):
        test_container = UIContainer(relative_rect=pygame.Rect(100, 100, 300, 60),
                                     manager=default_ui_manager)
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        container=test_container,
                        manager=default_ui_manager)

        label.set_relative_position((50, 50))

        assert label.rect.topleft == (150, 150)

    def test_set_dimensions(self, _init_pygame, default_ui_manager,
                            _display_surface_return_none):
        test_container = UIContainer(relative_rect=pygame.Rect(100, 100, 300, 60),
                                     manager=default_ui_manager)
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        container=test_container,
                        manager=default_ui_manager)

        label.set_dimensions((200, 50))

        assert label.rect.size == (200, 50)

    def test_disable(self, _init_pygame: None, default_ui_manager: UIManager,
                     _display_surface_return_none: None):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager)

        label.disable()

        assert label.is_enabled is False

    def test_enable(self, _init_pygame: None, default_ui_manager: UIManager,
                    _display_surface_return_none: None):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager)

        label.disable()
        label.enable()

        assert label.is_enabled is True

    def test_show(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager,
                        visible=0)

        assert label.visible == 0
        label.show()
        assert label.visible == 1

    def test_hide(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        label = UILabel(relative_rect=pygame.Rect(100, 100, 150, 30),
                        text="Test Label",
                        manager=default_ui_manager)

        assert label.visible == 1
        label.hide()
        assert label.visible == 0

    def test_show_hide_rendering(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        resolution = (400, 400)
        empty_surface = pygame.Surface(resolution)
        empty_surface.fill(pygame.Color(0, 0, 0))

        surface = empty_surface.copy()
        manager = UIManager(resolution)
        label = UILabel(relative_rect=pygame.Rect(25, 25, 375, 150),
                        text="Test Button",
                        manager=manager, visible=0)
        manager.update(0.01)
        manager.draw_ui(surface)
        assert compare_surfaces(empty_surface, surface)

        surface.fill(pygame.Color(0, 0, 0))
        label.show()
        manager.update(0.01)
        manager.draw_ui(surface)
        assert not compare_surfaces(empty_surface, surface)

        surface.fill(pygame.Color(0, 0, 0))
        label.hide()
        manager.update(0.01)
        manager.draw_ui(surface)
        assert compare_surfaces(empty_surface, surface)


if __name__ == '__main__':
    pytest.console_main()
