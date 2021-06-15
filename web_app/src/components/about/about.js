import React from 'react';
import Menu from '../common/menu'
import './about.css';
export default function About() {
    return (
        <div className="body-pd">
            <Menu></Menu>
            <div className="container-fluid">

                <h2 className='Title '> About us </h2>
                <h5 className='paragraph '>Quick report is a Web and Mobile application for all insurance companies and their clients. Launched in 2021, Quick Report’ unique strategy has established it as the go to source of the many problems we had in Tunisia when it comes to the traffic accident procedures. Our service is futuristic and very flexible since it's meant to make paper work from history. We work as a team with creative, motivated and ambitious members looking for a brighter future.
            </h5>

            <h3 className='subtitle '>Team</h3>

                <div className="row">

                    <div className="col">

                        <ul className="shadow"> <div className="h4"> Ahmed Belhaj</div>
                            <li><a href={'https://github.com/Theemiss'}> <i class="fab fa-github"> Themis</i></a></li>
                            <li><a href={'midinfotn401@gmail.com'}> <i class="fas fa-envelope-open"> Ahmed </i></a></li>
                        </ul>



                    </div>

                    <div className="col">

                        <ul className="shadow"> <div className="h4"> Amin Bondi </div>
                            <li><a href={'https://github.com/aminbnd'}> <i class="fab fa-github"> bondi</i> </a></li>
                            <li><a href={'aminbondi.holberton@gmail.com'}><i class="fas fa-envelope-open">  bondi</i></a></li>
                        </ul>
                    </div>

                    <div className="col">

                        <ul className="shadow"><div className="h4"> Mohamed Chedly </div>
                            <li><a href={'https://github.com/chedly99'}><i class="fab fa-github"> chdl</i></a></li>
                            <li id="contact"><a href={'mohamed.chedliiy@gmail.com'}><i class="fas fa-envelope-open">  chdl.</i></a></li>

                        </ul>

                    </div>



                </div>
                <h3 className='subtitle '>Contact Us</h3>
            <h5> WE ARE OPEN TO WORK,
                so if you are interested in any collaboration with us contact us     <a href='#contact'>Here</a> </h5>


            </div>
        </div>
    )
};