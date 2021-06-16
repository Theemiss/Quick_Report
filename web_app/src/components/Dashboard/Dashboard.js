import React from "react";
import Menu from "../common/menu";
import "./Dashboard.css";
import ChartistGraph from "react-chartist";
import { Row, Col } from "react-bootstrap";
var dataPie = {
  labels: ["62%", "32%", "6%"],
  series: [62, 32, 6],
};



// Data for Bar Chart
var dataBar = {
  labels: [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "Mai",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ],
  series: [
    [20, 100, 199, 200, 204, 300, 425, 503, 700, 900, 1000, 1500],
    [412, 243, 280, 580, 453, 353, 300, 364, 368, 410, 636, 100],
  ],
};
var optionsBar = {
  seriesBarDistance: 10,
  axisX: {
    showGrid: false,
  },
  height: "245px",
};
var responsiveBar = [
  [
    "screen and (max-width: 640px)",
    {
      seriesBarDistance: 5,
      axisX: {
        labelInterpolationFnc: function (value) {
          return value[0];
        },
      },
    },
  ],
];

export default function Dashboard() {
  return (
    <div className="body-pd">
      <Menu></Menu>
      <h2 className="Title "> Quick Report </h2>
      <div className="container-fluid">
        <Row>
          <Col className="box h4">
            <div className="box-title"> Number Client</div>
            <ul>
              <li>
                <span>All :</span> 1500
              </li>
              <br />
              <li>
                <span>New :</span> 20
              </li>
            </ul>
          </Col>
          <Col className="box h4">
            <div className="box-title"> Reports</div>
            <ul>
              <li>
                <span>All :</span> 100
              </li>
              <br />
              <li>
                <span>New :</span> 12
              </li>
            </ul>
          </Col>
          <Col className="box h4">
            <div className="box-title"> Feedback Awaiting</div>
            <ul>
              <li>
                <span>All :</span> 20
              </li>
              <br />
              <li>
                <span>New :</span> 2
              </li>
            </ul>
          </Col>
          <div className="col data" style={{ maxHeight: "320px" }}>
            <ChartistGraph data={dataPie} type="Pie" />
            <div>Red : Report Done</div>
            <div>Blue : Under Review</div>
            <div>Yellow : Wrong Info</div>

          </div>
          
        </Row>

        <div className=" data">
          <div className="col" style={{ maxHeight: "320px" }}>
            <ChartistGraph
              data={dataBar}
              type="Bar"
              options={optionsBar}
              responsiveOptions={responsiveBar}
            />
            <div>Red : Client</div>
            <div>Blue : Report</div>


          </div>
        </div>
          <div className=" data">
            <div className="col">
              <div className="box-title h4"> Updates</div>
              <ul>
                <li>
                  Coming soon
                </li>
                <br />
                <li>
                  
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
  );
}
