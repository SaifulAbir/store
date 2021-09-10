import React from "react";
import { Component } from "react";
import { Switch, Route } from "react-router-dom";
import {
  PRODUCT,
} from "./paths";
import Product from "../pages/Product";

class Routes extends Component {
  render() {
    return (
      <Switch>
        <Route exact path={PRODUCT}>
          <Product />
        </Route>
      </Switch>
    );
  }
}

export default Routes;
