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

import { MainSliderViewBlock, MainSliderEditBlock } from '@package/components';
import sliderSVG from '@plone/volto/icons/slider.svg';
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
  config.blocks.blocksConfig.mainslider = {
    id: 'mainslider',
    title: 'Main Slider',
    icon: sliderSVG,
    group: 'common',
    view: MainSliderViewBlock,
    edit: MainSliderEditBlock,
    restricted: false,
    mostUsed: true,
    security: {
      addPermission: [],
      view: [],
    },
  };

  // Add here your project's configuration here by modifying `config` accordingly
  return config;
}
