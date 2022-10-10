import Slider from 'react-slick';
import slide1 from './slide1.jpeg';
import slide2 from './slide2.jpeg';
import slide3 from './slide3.jpg';

const View = (props) => {
  var settings = {
    outerWidth: 40,
    className: "center",
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
