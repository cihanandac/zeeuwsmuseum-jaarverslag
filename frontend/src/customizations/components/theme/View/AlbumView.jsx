/**
 * Album view component.
 * @module components/theme/View/AlbumView
 */
import { getBaseUrl, applyBlockDefaults } from '@plone/volto/helpers';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Container, GridColumn, Segment } from 'semantic-ui-react';
import { Button, Modal, Grid } from 'semantic-ui-react';
import { Icon, UniversalLink, PreviewImage } from '@plone/volto/components';
import config from '@plone/volto/registry';
import { map } from 'lodash';
import openSVG from '@plone/volto/icons/open.svg';
import aheadSVG from '@plone/volto/icons/ahead.svg';
import backSVG from '@plone/volto/icons/back.svg';
import {
  getBlocksFieldname,
  getBlocksLayoutFieldname,
  hasBlocksData,
} from '@plone/volto/helpers';

/**
 * Album view component class.
 * @function AlbumView
 * @param {Object} content Content object.
 * @returns {string} Markup of the component.
 */



class AlbumView extends Component {
  constructor(props) {
    super(props);

    this.state = {
      openIndex: undefined,
    };

    this.closeModal = this.closeModal.bind(this);
    this.nextImage = this.nextImage.bind(this);
    this.prevImage = this.prevImage.bind(this);
  }

  closeModal() {
    this.setState({
      openIndex: -1,
    });
  }

  nextImage() {
    const openIndex =
      (this.state.openIndex + 1) % this.props.content.items.length;
    this.setState({
      openIndex,
    });
  }

  prevImage() {
    const openIndex =
      (this.state.openIndex - 1) % this.props.content.items.length;
    this.setState({
      openIndex,
    });
  }

  

  render() {
    // const { content } = this.props;
    const { location, intl, content, metadata } = this.props;
    const blocksFieldname = getBlocksFieldname(content);
    const blocksLayoutFieldname = getBlocksLayoutFieldname(content);
    const blocksConfig = this.props.blocksConfig || config.blocks.blocksConfig;
    const CustomTag = `${this.props.as || 'div'}`;
    return hasBlocksData(content) ? (
      <CustomTag>
        {map(content[blocksLayoutFieldname].items, (block) => {
          const Block =
            blocksConfig[content[blocksFieldname]?.[block]?.['@type']]?.view;

          const blockData = applyBlockDefaults({
            data: content[blocksFieldname][block],
            intl,
            metadata,
            properties: content,
          });

          return Block ? (
            <Block
              key={block}
              id={block}
              metadata={metadata}
              properties={content}
              data={blockData}
              path={getBaseUrl(location?.pathname || '')}
              blocksConfig={blocksConfig}
            />
          ) : (
            <div key={block}>
              {intl.formatMessage(messages.unknownBlock, {
                block: content[blocksFieldname]?.[block]?.['@type'],
              })}
            </div>
          );
        })}
      </CustomTag>
    ) : (
      ''
    );
  }
}

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
AlbumView.propTypes = {
  /**
   * Content of the object
   */
  content: PropTypes.shape({
    /**
     * Title of the object
     */
    title: PropTypes.string,
    /**
     * Description of the object
     */
    description: PropTypes.string,
    /**
     * Child items of the object
     */
    items: PropTypes.arrayOf(
      PropTypes.shape({
        /**
         * Title of the item
         */
        title: PropTypes.string,
        /**
         * Description of the item
         */
        description: PropTypes.string,
        /**
         * Url of the item
         */
        url: PropTypes.string,
        /**
         * Image of the item
         */
        image: PropTypes.object,
        /**
         * Image caption of the item
         */
        image_caption: PropTypes.string,
        /**
         * Type of the item
         */
        '@type': PropTypes.string,
      }),
    ),
  }).isRequired,
};

export default AlbumView;
