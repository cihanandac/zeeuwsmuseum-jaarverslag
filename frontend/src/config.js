/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */

import {
  SocialTopViewBlock,
  SocialTopEditBlock,
  EmptylineEditBlock,
  EmptylineViewBlock,
  SocialBottomViewBlock,
  SocialBottomEditBlock,
  NutezienViewBlock,
  NutezienEditBlock,
} from '@package/components';
import sliderSVG from '@plone/volto/icons/slider.svg';
import dotsSVG from '@plone/volto/icons/dots.svg';
// import { defineMessages } from 'react-intl';
// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

// defineMessages({
//   mainslider: {
//     id: 'Main Slider',
//     defaultMessage: 'Main Slider',
//   },
// });

export default function applyConfig(config) {
  config.blocks.requiredBlocks = [];

  (config.blocks.blocksConfig.socialtop = {
    id: 'socialtop',
    title: 'Socialtop',
    icon: sliderSVG,
    group: 'common',
    view: SocialTopViewBlock,
    edit: SocialTopEditBlock,
    restricted: false,
    mostUsed: true,
    security: {
      addPermission: [],
      view: [],
    },
  }),
    (config.blocks.blocksConfig.socialbottom = {
      id: 'socialbottom',
      title: 'Socialbottom',
      icon: sliderSVG,
      group: 'common',
      view: SocialBottomViewBlock,
      edit: SocialBottomEditBlock,
      restricted: false,
      mostUsed: true,
      security: {
        addPermission: [],
        view: [],
      },
    }),
    (config.blocks.blocksConfig.emptyline = {
      id: 'emptyline',
      title: 'Empty Line',
      icon: dotsSVG,
      group: 'text',
      view: EmptylineViewBlock,
      edit: EmptylineEditBlock,
      restricted: false,
      mostUsed: true,
      security: {
        addPermission: [],
        view: [],
      },
    }),
    (config.blocks.blocksConfig.nutezien = {
      id: 'nutezien',
      title: 'Nutezien',
      icon: sliderSVG,
      group: 'common',
      view: NutezienViewBlock,
      edit: NutezienEditBlock,
      restricted: false,
      mostUsed: true,
      security: {
        addPermission: [],
        view: [],
      },
    });

  // Add here your project's configuration here by modifying `config` accordingly
  return config;
}
