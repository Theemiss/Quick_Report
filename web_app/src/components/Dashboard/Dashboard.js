import React, { useEffect, useState } from "react";
import useToken from "../app/useToken";
import Menu from "../common/menu";
import "./Dashboard.css";
import ChartistGraph from "react-chartist";
import { Row, Col } from "react-bootstrap";

export default function Dashboard() {
  const { token, setToken } = useToken();
  const [data, setData] = useState({});
  const Token = "Bearer ".concat(token);

  const url = "http://102.37.113.211/api/company/data";
  useEffect(() => {
    const fetchUserInfo = async () => {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: Token,
        },
      });

      const email = await response.json();

      setData(email);
    };
    fetchUserInfo();
    // eslint-disable-next-line
  }, []);
  var dataPie = {
    labels: ["0%", "100%", "0%"],
    series: [0, 100, 0],
  };

  var labels = [
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
  ];

  var series = [
    [0, 0, 0, 0, 0, data.user, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, data.report, 0, 0, 0, 0, 0, 0],
  ];

  // Data for Bar Chart
  var dataBar = {
    labels,
    series,
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
                <span>All :</span> {data.user}
              </li>
              <br />
              <li>
                <span>New :</span> Coming soon
              </li>
            </ul>
          </Col>
          <Col className="box h4">
            <div className="box-title"> Reports</div>
            <ul>
              <li>
                <span>All :</span> {data.report}
              </li>
              <br />
              <li>
                <span>New :</span> Coming soon
              </li>
            </ul>
          </Col>
          <Col className="box h4">
            <div className="box-title"> Feedback Awaiting</div>
            <ul>
              <li>
                <span>All :</span> Coming soon
              </li>
              <br />
              <li>
                <span>New :</span> Coming soon
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
              <li>Coming soon</li>
              <br />
              <li></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
