import React from 'react';
import Slider from 'react-slick';


const View = (props) => {
  var settings = {
    outerWidth: 40,
    className: 'center',
    centerMode: true,
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <Slider {...settings}>
      {/* <div>
        <img src="$(slide1)" alt="" />
      </div>
      <div>
        <img src="$(slide2)" alt="" />
      </div>
      <div>
        <img src="$(slide3)" alt="" />
      </div> */}
    </Slider>
  );
};

export default View;
