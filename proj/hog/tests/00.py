test = {
  'name': 'Question 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = make_test_dice(4, 1, 2)
          >>> test_dice()
          4
          >>> test_dice() # Second call
          1
          >>> test_dice() # Third call
          2
          >>> test_dice() # Fourth call
          4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'answer': '5c489e1123a9d0cfdd0c26a27a56d42b',
          'choices': [
            'make_test_dice(6)',
            'make_fair_dice(6)',
            'six_sided',
            'six_sided()'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following is the correct way to "roll" a fair, six-sided die?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
