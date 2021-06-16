import react from "react";
import Menu from "../common/menu";
import './Dashboard.css';
export default function Dashboard() {
    return (
        <div className="body-pd">
        <Menu></Menu>
            <h2 className='Title '> Quick Report </h2>

  <div class="row1-container">
    <div class="box box-down cyan">
      <h2>1</h2>
      <p>1</p>
    </div>

    <div class="box red">
      <h2>2</h2>
      <p>2</p>
    </div>

    <div class="box box-down blue">
      <h2>3</h2>
      <p>3</p>
    </div>
  </div>

  <div class="row2-container">
    <div class="box orange">
      <h2>4</h2>
      <p>4</p>
    </div>
  </div>

        </div>
    )
};