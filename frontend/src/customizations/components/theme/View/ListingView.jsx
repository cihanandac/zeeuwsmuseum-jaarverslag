/**
 * Document view component.
 * @module components/theme/View/ListingView
 */

import React from 'react';
import PropTypes from 'prop-types';
import { Segment, Container } from 'semantic-ui-react';
import { UniversalLink, PreviewImage } from '@plone/volto/components';

/**
 * List view component class.
 * @function ListingView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const ListingView = ({ content }) => (
  <Container id="page-home">
    <div id="list-title">
      <h1>{content.title}</h1>
    </div>
    <section id="content-core">
      {content.items.map((item) => (
        <Segment key={item.url} className="listing-item">
          {item.image_field && (
            <UniversalLink item={item}>
              <PreviewImage
                item={item}
                size="large"
                alt={item.image_caption ? item.image_caption : item.title}
                className="ui image"
              />
            </UniversalLink>
          )}
          <Container>
            <h2>
              <UniversalLink item={item}>
                JAARVERSLAG {item.title}
              </UniversalLink>
            </h2>
            {item.description && <p>{item.description}</p>}
          </Container>
        </Segment>
      ))}
    </section>
  </Container>
);

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
ListingView.propTypes = {
  content: PropTypes.shape({
    title: PropTypes.string,
    description: PropTypes.string,
    items: PropTypes.arrayOf(
      PropTypes.shape({
        '@id': PropTypes.string,
        '@type': PropTypes.string,
        description: PropTypes.string,
        review_state: PropTypes.string,
        title: PropTypes.string,
        url: PropTypes.string,
      }),
    ),
  }).isRequired,
};

export default ListingView;
