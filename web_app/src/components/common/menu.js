
import React from 'react';
import { Link } from 'react-router-dom';

import './menu.css'
export default function Menu() {

    return (
        <div>
           
            <div className="l-navbar show" id="nav-bar">
                <nav className="nav">
                    <div> <Link to="/" className="nav_logo">
                         <i className='bx bx-layer nav_logo-icon'></i> <span className="nav_logo-name">Quick Report</span>
                          </Link>
                         
                        <div className="nav_list"> <Link to="/" className="nav_link active"> 
                        <i className='bx bx-grid-alt nav_icon'></i> <span className="nav_name">Dashboard</span> 

                        </Link> <Link to="clients" className="nav_link"> <i class='bx bx-user nav_icon'></i> 
                        <span class="nav_name">Users</span> </Link> <Link to="reports" class="nav_link">
                             <i class='bx bx-message-square-detail nav_icon'></i> <span class="nav_name">Report</span>
                              </Link>  </div>
                    </div> <Link to="/logout" className="nav_link"> <i className='bx bx-log-out nav_icon'></i> 
                    <span className="nav_name">SignOut</span> </Link>
                </nav>
            </div>

        </div>
    )
};



