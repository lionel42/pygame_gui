import pygame
import pygame.freetype
import pytest

from pygame_gui.ui_manager import UIManager
from pygame_gui.core.text import  HyperlinkTextChunk


class TestTextBoxLayout:
    def test_creation(self, _init_pygame, default_ui_manager: UIManager):
        the_font = pygame.freetype.Font(None, 20)
        style = {'link_text':       pygame.Color('#FF0000'),
                 'bg_colour':       pygame.Color('#808080'),
                 'link_hover':      pygame.Color('#FF00FF'),
                 'link_selected':   pygame.Color('#FFFF00'),
                 'link_hover_underline': False,
                 'shadow_data': None}

        HyperlinkTextChunk('link_target',
                           'test link',
                           the_font,
                           False,
                           colour=style['link_text'],
                           bg_colour=style['bg_colour'],
                           hover_colour=style['link_hover'],
                           selected_colour=style['link_selected'],
                           hover_underline=style['link_hover_underline'],
                           text_shadow_data=style['shadow_data'])

    def test_on_hovered(self, _init_pygame, default_ui_manager: UIManager):
        the_font = pygame.freetype.Font(None, 20)
        style = {'link_text':       pygame.Color('#FF0000'),
                 'bg_colour':       pygame.Color('#808080'),
                 'link_hover':      pygame.Color('#FF00FF'),
                 'link_selected':   pygame.Color('#FFFF00'),
                 'link_hover_underline': False,
                 'shadow_data': None}

        hyper_chunk = HyperlinkTextChunk('link_target',
                                         'test link',
                                         the_font,
                                         False,
                                         colour=style['link_text'],
                                         bg_colour=style['bg_colour'],
                                         hover_colour=style['link_hover'],
                                         selected_colour=style['link_selected'],
                                         hover_underline=style['link_hover_underline'],
                                         text_shadow_data=style['shadow_data'])

        rendered_chunk_surf = pygame.Surface((200, 30))
        rendered_chunk_surf.fill((0, 0, 0))
        hyper_chunk.finalise(target_surface=rendered_chunk_surf,
                             target_area=pygame.Rect(0, 0, 200, 30),
                             row_chunk_origin=0,
                             row_chunk_height=20,
                             row_bg_height=20)

        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF0000')
        hyper_chunk.on_hovered()
        assert hyper_chunk.is_hovered
        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF00FF')

    def test_on_unhovered(self, _init_pygame, default_ui_manager: UIManager):
        the_font = pygame.freetype.Font(None, 20)
        style = {'link_text':       pygame.Color('#FF0000'),
                 'bg_colour':       pygame.Color('#808080'),
                 'link_hover':      pygame.Color('#FF00FF'),
                 'link_selected':   pygame.Color('#FFFF00'),
                 'link_hover_underline': False,
                 'shadow_data': None}

        hyper_chunk = HyperlinkTextChunk('link_target',
                                         'test link',
                                         the_font,
                                         False,
                                         colour=style['link_text'],
                                         bg_colour=style['bg_colour'],
                                         hover_colour=style['link_hover'],
                                         selected_colour=style['link_selected'],
                                         hover_underline=style['link_hover_underline'],
                                         text_shadow_data=style['shadow_data'])

        rendered_chunk_surf = pygame.Surface((200, 30))
        rendered_chunk_surf.fill((0, 0, 0))
        hyper_chunk.finalise(target_surface=rendered_chunk_surf,
                             target_area=pygame.Rect(0, 0, 200, 30),
                             row_chunk_origin=0,
                             row_chunk_height=20,
                             row_bg_height=20)

        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF0000')
        hyper_chunk.on_hovered()
        assert hyper_chunk.is_hovered
        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF00FF')
        hyper_chunk.on_unhovered()
        assert not hyper_chunk.is_hovered
        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF0000')

    def test_on_selected(self, _init_pygame, default_ui_manager: UIManager):
        the_font = pygame.freetype.Font(None, 20)
        style = {'link_text':       pygame.Color('#FF0000'),
                 'bg_colour':       pygame.Color('#808080'),
                 'link_hover':      pygame.Color('#FF00FF'),
                 'link_selected':   pygame.Color('#FFFF00'),
                 'link_hover_underline': False,
                 'shadow_data': None}

        hyper_chunk = HyperlinkTextChunk('link_target',
                                         'test link',
                                         the_font,
                                         False,
                                         colour=style['link_text'],
                                         bg_colour=style['bg_colour'],
                                         hover_colour=style['link_hover'],
                                         selected_colour=style['link_selected'],
                                         hover_underline=style['link_hover_underline'],
                                         text_shadow_data=style['shadow_data'])

        rendered_chunk_surf = pygame.Surface((200, 30))
        rendered_chunk_surf.fill((0, 0, 0))
        hyper_chunk.finalise(target_surface=rendered_chunk_surf,
                             target_area=pygame.Rect(0, 0, 200, 30),
                             row_chunk_origin=0,
                             row_chunk_height=20,
                             row_bg_height=20)

        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF0000')
        hyper_chunk.on_selected()
        assert hyper_chunk.is_selected
        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FFFF00')

    def test_on_unselected(self, _init_pygame, default_ui_manager: UIManager):
        the_font = pygame.freetype.Font(None, 20)
        style = {'link_text':       pygame.Color('#FF0000'),
                 'bg_colour':       pygame.Color('#808080'),
                 'link_hover':      pygame.Color('#FF00FF'),
                 'link_selected':   pygame.Color('#FFFF00'),
                 'link_hover_underline': False,
                 'shadow_data': None}

        hyper_chunk = HyperlinkTextChunk('link_target',
                                         'test link',
                                         the_font,
                                         False,
                                         colour=style['link_text'],
                                         bg_colour=style['bg_colour'],
                                         hover_colour=style['link_hover'],
                                         selected_colour=style['link_selected'],
                                         hover_underline=style['link_hover_underline'],
                                         text_shadow_data=style['shadow_data'])

        rendered_chunk_surf = pygame.Surface((200, 30))
        rendered_chunk_surf.fill((0, 0, 0))
        hyper_chunk.finalise(target_surface=rendered_chunk_surf,
                             target_area=pygame.Rect(0, 0, 200, 30),
                             row_chunk_origin=0,
                             row_chunk_height=20,
                             row_bg_height=20)

        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF0000')
        hyper_chunk.on_selected()
        assert hyper_chunk.is_selected
        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FFFF00')
        hyper_chunk.on_unselected()
        assert not hyper_chunk.is_selected
        assert rendered_chunk_surf.get_at((1, 5)) == pygame.Color('#FF0000')


if __name__ == '__main__':
    pytest.console_main()
