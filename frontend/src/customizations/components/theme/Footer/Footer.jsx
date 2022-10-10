/**
 * Footer component.
 * @module components/theme/Footer/Footer
 */

import React from 'react';
import { Container, List, Segment } from 'semantic-ui-react';
import { Logo } from '@plone/volto/components';
import { FormattedMessage, defineMessages, injectIntl } from 'react-intl';
import { useSelector } from 'react-redux';
import { UniversalLink } from '@plone/volto/components';
import config from '@plone/volto/registry';

const messages = defineMessages({
  copyright: {
    id: 'Copyright',
    defaultMessage: 'Copyright',
  },
});

/**
 * Component to display the footer.
 * @function Footer
 * @param {Object} intl Intl object
 * @returns {string} Markup of the component
 */
const Footer = ({ intl }) => {
  const { settings } = config;
  const lang = useSelector((state) => state.intl.locale);
  return (
    <container id="footer">
      <div id="top-footer">
        <div className="footerInfoBox">
          <a className='footerHeader' href="#">BEZOKADRES</a>
          <p>Abdij (Plein)</p>
          <p>4331 BK, Middleburg</p>
        </div>
        <div className="footerInfoBox">
          <a href="#">CONTACT ALGEMEEN</a>
          <p>+31 (0) 118 653000</p>
          <a href="info@zeeuwsmuseum.nl">info@zeeuwsmuseum.nl</a>
        </div>
        <div id='footermail' className="footerInfoBox">
          <a href="#">NIEUWSBRIEF</a>
          <p> Schrijf je in voor onze nieuwsbrief en blijf op de hoogte. </p>
        </div>
      </div>
      <div id='bottom-footer'>
        <div id="footerdown">
          <Logo id="footerLogo" />
        </div>
      </div>
    </container>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
Footer.propTypes = {
  /**
   * i18n object
   */
};

export default injectIntl(Footer);
