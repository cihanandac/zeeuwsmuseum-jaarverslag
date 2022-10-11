import React, { Component } from 'react';
import { BsChevronDown } from 'react-icons/bs';

class SubmenuPlan extends React.Component {
  render() {
    return (
      <ul className="nav__submenu">
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/praktische-info">
            Praktische informatie
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/nu-in-het-museum">
            Zien en doen
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/kinderen-klas-of-groep">
            Families, groupen en scholen
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/leukdagjeuit">
            Dagje uit Middelburg
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/boek-je-bezoek">
            Boek je bezoek
          </a>
        </li>
      </ul>
    );
  }
}
class SubmenuOntdek extends React.Component {
  render() {
    return (
      <ul className="nav__submenu">
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/videotheek">Videotheek</a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/collectie/mode-en-streekdracht">
            Mode en streekdracht
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/collectie/wandtapijten">
            Wandtapijten
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/collectie/geschiedenis-en-archeologie">
            Geschiedenis en archeologie
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/collectie/kunst">Kunst</a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/collectie/kunstnijverheid">
            Kunstnijverheid
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/collectie/natuurhistorie">
            Natuurhistorie
          </a>
        </li>
      </ul>
    );
  }
}
class SubmenuOver extends React.Component {
  render() {
    return (
      <ul className="nav__submenu">
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/over-het-museum/steun-het-museum">
            Steun het museum
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/over-het-museum/pers">Pers</a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/over-het-museum/organisatie">
            Organisatie
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/over-het-museum/publicaties">
            Publicaties
          </a>
        </li>
        <li className="nav__submenu-item ">
          <a href="https://www.zeeuwsmuseum.nl/nl/over-het-museum/voorwaarden">
            Voorwaarden
          </a>
        </li>
      </ul>
    );
  }
}

class Menu extends React.Component {
  render() {
    return (
      <nav className="nav">
        <ul className="nav__menu">
          <li className="nav__menu-item">
            <a href="http://volto.cihanandac.net">JAARVERSLAG</a>
          </li>
          <li className="nav__menu-item">
            <a>
              PLAN JE BEZOEK <BsChevronDown />
            </a>
            <SubmenuPlan />
          </li>
          <li className="nav__menu-item">
            <a>
              ONTDEK <BsChevronDown />
            </a>
            <SubmenuOntdek />
          </li>
          <li className="nav__menu-item">
            <a>
              OVER HET MUSEUM <BsChevronDown />
            </a>
            <SubmenuOver />
          </li>
          <li className="nav__menu-item">
            <a href="https://www.zeeuwsmuseum.nl/nl/plan-je-bezoek/boek-je-bezoek">
              TICKETS
            </a>
          </li>
        </ul>
      </nav>
    );
  }
}

export default Menu;
