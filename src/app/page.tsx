import React from "react"

import { Metadata, NextPage } from "next"

import { Home } from "@/views"

interface HomePageProps {}

export const metadata: Metadata = {
  title: "Home page",
  description: "Home page",
}

const HomePage: NextPage<HomePageProps> = () => {
  return (
    <>
      <Home.Landing />
    </>
  )
}

export default HomePage
