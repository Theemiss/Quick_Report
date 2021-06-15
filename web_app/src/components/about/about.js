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
            <h3 className='subtitle '>Contact Us</h3>
            <h5> WE ARE OPEN TO WORK,
                so if you are interested in any collaboration with us contact us here: </h5>

                <div className="row">
                    <div className="col">
                    <div> Ahmed Belhaj</div>
                        <ul>
                            <li><a href={'https://github.com/Theemiss'}> github bo7.</a></li>
                            <li><a href={'midinfotn401@gmail.com'}> email bo7.</a></li>
                        </ul>
                   


                    </div>

                    <div className="col">
                    <div> Amin Bondi </div>
                    <ul>
            <li><a href={'https://github.com/aminbnd'}> github bondi.</a></li>
            <li><a href={'aminbondi.holberton@gmail.com'}> email bondi.</a></li>
                    </ul>
                    </div>

                    <div className="col">
                    <div> Mohamed Chedly </div>
                    <ul>
                        <li><a href={'https://github.com/chedly99'}> email chdl.</a></li>
                        <li><a href={'mohamed.chedliiy@gmail.com'}> emai chdl.</a></li>

                        </ul>
      
                    </div>
            
            
           
            </div>
            
            </div>
            </div>
    )
};