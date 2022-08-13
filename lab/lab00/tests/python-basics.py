test = {
  'name': 'Python Basics',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 10 + 2
          12
          >>> 7 / 2
          3.5
          >>> 7 // 2
          3
          >>> 7 % 2			# 7 modulo 2, the remainder when dividing 7 by 2.
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> x = 20
          >>> x + 2
          22
          >>> x
          20
          >>> y = 5
          >>> y = y + 3
          >>> y * 2
          309984ef0dc06025a91b127042939a0e
          # locked
          >>> y = y // 4
          >>> y + x
          3d3ab69a0677d75a0ef4a99e0d2d1451
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
