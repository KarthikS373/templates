import React from "react"

import { NextPage } from "next"

interface FeedsLayoutProps {
  children: React.ReactNode
  modal: React.ReactNode
}

const FeedsLayout: NextPage<FeedsLayoutProps> = ({ children, modal }) => {
  return (
    <div>
      <div className="center min-h-screen">
        <>{children}</>
      </div>
      {modal}
    </div>
  )
}

export default FeedsLayout
