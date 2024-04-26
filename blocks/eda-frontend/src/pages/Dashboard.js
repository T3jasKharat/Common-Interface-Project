// Main Layout for user dashboard.
import React, { useEffect } from 'react'
import { Switch } from 'react-router-dom'
import { CompatRoute } from 'react-router-dom-v5-compat'
import { CssBaseline } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'

import { Header } from '../components/Shared/Navbar'
import Layout from '../components/Shared/Layout'
import LayoutMain from '../components/Shared/LayoutMain'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar'
import DashboardHome from '../components/Dashboard/DashboardHome'
import SchematicsList from '../components/Dashboard/SchematicsList'

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    minHeight: '100vh'
  },
  toolbar: {
    minHeight: '40px'
  }
}))

export default function Dashboard () {
  const classes = useStyles()

  useEffect(() => {
    document.title = 'Dashboard - ' + process.env.REACT_APP_NAME
  })

  return (
    <div className={classes.root}>
      <CssBaseline />

      {/* Schematic editor header and left side pane */}
      <Layout resToolbar={<Header />} sidebar={<DashboardSidebar />} />

      <LayoutMain>
        <div className={classes.toolbar} />

        {/* Subroutes under dashboard section */}
        <Switch>
          <CompatRoute exact path='/dashboard' component={DashboardHome} />
          <CompatRoute exact path='/dashboard/profile' />
          <CompatRoute
            exact
            path='/dashboard/schematics'
            component={SchematicsList}
          />
        </Switch>
      </LayoutMain>
    </div>
  )
}
