/**
 * Breadcrumbs components.
 * @module components/theme/Breadcrumbs/Breadcrumbs
 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { Link } from 'react-router-dom';
import { Breadcrumb, Container, Segment } from 'semantic-ui-react';
import { defineMessages, injectIntl } from 'react-intl';
import { Icon } from '@plone/volto/components';
import { getBreadcrumbs } from '@plone/volto/actions';
import { getBaseUrl, hasApiExpander } from '@plone/volto/helpers';
import { BsChevronCompactRight } from 'react-icons/bs';
import NavItems from '@plone/volto/components/theme/Navigation/NavItems';
import { getNavigation } from '@plone/volto/actions';
import { Dropdown, Menu, Accordion, Form } from 'semantic-ui-react';
import { FaChevronDown } from 'react-icons/fa';

import homeSVG from '@plone/volto/icons/home.svg';

const messages = defineMessages({
  home: {
    id: 'Home',
    defaultMessage: 'Home',
  },
  breadcrumbs: {
    id: 'Breadcrumbs',
    defaultMessage: 'Breadcrumbs',
  },
});

/**
 * Breadcrumbs container class.
 */
export class BreadcrumbsComponent extends Component {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */

  static propTypes = {
    getBreadcrumbs: PropTypes.func.isRequired,
    pathname: PropTypes.string.isRequired,
    root: PropTypes.string,
    items: PropTypes.arrayOf(
      PropTypes.shape({
        title: PropTypes.string,
        url: PropTypes.string,
      }),
    ).isRequired,
  };

  componentDidMount() {
    if (!hasApiExpander('breadcrumbs', getBaseUrl(this.props.pathname))) {
      this.props.getBreadcrumbs(getBaseUrl(this.props.pathname));
    }
  }

  /**
   * Component will receive props
   * @method componentWillReceiveProps
   * @param {Object} nextProps Next properties
   * @returns {undefined}
   */
  UNSAFE_componentWillReceiveProps(nextProps) {
    if (nextProps.pathname !== this.props.pathname) {
      if (!hasApiExpander('breadcrumbs', getBaseUrl(this.props.pathname))) {
        this.props.getBreadcrumbs(getBaseUrl(nextProps.pathname));
      }
    }
  }

  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */
  render() {
    return (
      <Segment
        role="navigation"
        aria-label={this.props.intl.formatMessage(messages.breadcrumbs)}
        className="breadcrumbs"
        secondary
        vertical
      >
        {/* {console.log(
          this.props.items.map((item, index, items) => [item.title]),
        )} */}

        {/* {console.log(
          this.props.items[2]
        )} */}

        {/* {console.log(<NavItems items={this.props.intl} />)} */}
        {console.log(<NavItems items={this.props.items} />)}

        <Container id="crumbcontainer">
          <Breadcrumb id="folderMap">
            <Link
              to={this.props.root || '/'}
              className="section"
              title={this.props.intl.formatMessage(messages.home)}
            >
              {/* <Icon name={homeSVG} size="25px" /> */}
            </Link>
            {this.props.items.map((item, index, items) => [
              ,
              index < items.length - 1 ? (
                <Link key={item.url} to={item.url} className="section">
                  {item.title}
                  <span>&nbsp;</span>
                </Link>
              ) : (
                <Breadcrumb.Section
                  className="crumbcontainer"
                  key={item.url}
                  active
                >
                  <Breadcrumb.Divider className="breaddivider">
                    <BsChevronCompactRight
                      stroke="white"
                      fill="currentColor"
                      strokeWidth="0.5"
                    />
                  </Breadcrumb.Divider>
                  <div className="breadtitle">
                    <span>{item.title}</span>
                  </div>
                </Breadcrumb.Section>
              ),
            ])}
          </Breadcrumb>
          <Container id="dropdowncontainer">
            <div id="inhoud">
              <Dropdown
                item
                simple
                text={ this.props.items.length > 2 ? this.props.items[2].title : "INHOUD"}
                icon={<FaChevronDown color="#808080" />}
              >
                <Dropdown.Menu className="dropdownContentPage">
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="../">Beeldimpressie </a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./terugblik">Terugblik</a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./inspireren-verwonderen">
                      Inspireren & Verwonderen
                    </a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./bewaren-verzamelen">Bewaren & Verzamelen</a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./leren-verbinden">Leren & Verbinden</a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./eenzm">eenZM</a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./financieel-verslag">Financieel verslag</a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./cultureel-ondernemerschap">
                      Cultureel Ondernemerschap
                    </a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./met-dank-aan">Met dank aan</a>
                  </Dropdown.Item>
                  <Dropdown.Item id="InhoudDropdown">
                    <a href="./colofon">Colofon</a>
                  </Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
            </div>
          </Container>
        </Container>
      </Segment>
    );
  }
}

export default compose(
  injectIntl,
  connect(
    (state) => ({
      items: state.breadcrumbs.items,
      root: state.breadcrumbs.root,
    }),
    { getBreadcrumbs },
  ),
)(BreadcrumbsComponent);
