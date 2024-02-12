"use client"

import React, { useEffect, useState } from "react"

import Link from "next/link"

const FeedsPage = () => {
  const [feeds, setFeeds] = useState<IIterable<{ id: number }>>([])

  useEffect(() => {
    // TODO: fetch feeds
    const _feeds = Array.from({ length: 10 }, (_, i) => ({
      id: i,
    }))

    setFeeds(_feeds)
  }, [])

  return (
    <div className="center min-h-screen">
      <div className="grid grid-cols-3 gap-8">
        {feeds.map((feed) => (
          <Link
            href={`/feeds/${feed.id}`}
            className="center aspect-square w-32 cursor-pointer bg-gray-400/25"
            key={feed.id}
          >
            <p>{feed.id}</p>
          </Link>
        ))}
      </div>
    </div>
  )
}

export default FeedsPage
