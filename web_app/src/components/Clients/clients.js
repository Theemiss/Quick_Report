import React, { useEffect, useState } from "react";
import Menu from "../common/menu";
import useToken from "../app/useToken";
import "./client.css";
import { Link } from "react-router-dom";
import ListGroup from "react-bootstrap/ListGroup";
import { Tab, Row, Col } from "react-bootstrap";
/**
 * 
 * @returns All Client Component
 */
export default function Clients() {
  // eslint-disable-next-line
  const { token, setToken } = useToken();
  const [data, setData] = useState({});
  const Token = "Bearer ".concat(token);

  useEffect(() => {
    const fetchClients = async () => {
      const response = await fetch(
        "http://102.37.113.211/api/company/clients",
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: Token,
          },
        }
      );

      const email = await response.json();

      setData(email);
    };

    fetchClients();
    // eslint-disable-next-line
  }, []);
  const arr = [];
  for (const x in data) {
    arr.push(data[x]);
  }
  let num = arr.length;
  return (
    <div className="body-pd">
      <Menu />
      <h2 className="Title">
        All Client <span class="badge bg gray-900 rounded-pill">{num}</span>{" "}
      </h2>
      <Tab.Container id="idlist-group-tabs-example">
        <Row>
          <Col sm={11}>
            {arr.map((user) => (
              <ListGroup className="Model_id">
                <Link to={{ pathname: `user/${user.id}` }}>
                  {" "}
                  <ListGroup.Item className="  shadow mb-2  ">
                    {user.email}
                  </ListGroup.Item>
                </Link>
              </ListGroup>
            ))}{" "}
          </Col>
        </Row>
      </Tab.Container>
    </div>
  );
}
