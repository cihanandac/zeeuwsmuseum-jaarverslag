import React from 'react';
import Slider from 'react-slick';
import { Link } from 'react-router-dom';
import { Button } from 'semantic-ui-react';
import { Icon } from '@plone/volto/components';
import sliderPNG from './slider-image.png';
import rightSVG from '@plone/volto/icons/right-key.svg';
import leftSVG from '@plone/volto/icons/left-key.svg';
import { withBlockExtensions } from '@plone/volto/helpers';

const NextArrow = ({ className, style, onClick }) => (
  <Button
    className={className}
    style={{ ...style, display: 'block' }}
    onClick={onClick}
  >
    <Icon name={rightSVG} size="70px" color="#fff" />
  </Button>
);

const PrevArrow = ({ className, style, onClick }) => (
  <Button
    className={className}
    style={{ ...style, display: 'block' }}
    onClick={onClick}
  >
    <Icon name={leftSVG} size="70px" color="#fff" />
  </Button>
);

const View = (props) => {
  return (
    <div
      className="block view mainslider full-width"
      style={{
        background: `url(${sliderPNG}) center no-repeat`,
      }}
    >
      <Slider
        customPaging={(dot) => <div />}
        dots={true}
        fade
        dotsClass="slick-dots slick-thumb"
        infinite
        speed={500}
        slidesToShow={1}
        slidesToScroll={1}
        nextArrow={<NextArrow />}
        prevArrow={<PrevArrow />}
      >
        <div>
          <div className="slide slide1">
            <h3>Plone</h3>
            <h1>
              The Ultimate <br />
              Open Source Enterprise CMS
            </h1>
            <Link to="/plone5">Learn about Plone 5</Link>
          </div>
        </div>
        <div>
          <div className="slide slide1">
            <h3>Plone 5.2</h3>
            <h1>
              The Future-Proofing Release: <br />
              Python 3 and REST API
            </h1>
            <Link to="/plone52">Learn about Plone 5.2</Link>
          </div>
        </div>
      </Slider>
    </div>
  );
};

export default withBlockExtensions(View);
