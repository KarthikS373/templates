import React from "react"

import { Metadata, NextPage } from "next"

interface HomePageProps {}

export const metadata: Metadata = {
  title: "Home page",
  description: "Home page",
}

const HomePage: NextPage<HomePageProps> = () => {
  return <></>
}

export default HomePage
