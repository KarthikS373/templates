import React from "react"

import { NextPage } from "next"

interface IndividualFeedPageProps {
  params: {
    id: string
  }
}

const IndividualFeedPage: NextPage<IndividualFeedPageProps> = ({ params: { id } }) => {
  return <div>Feed page for : Feed {id}</div>
}

export default IndividualFeedPage
