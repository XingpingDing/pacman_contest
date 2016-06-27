test = {
  'name': 'Memoization',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'd52e81ff797656c08d455ced1c208fe0',
          'choices': [
            'O(1)',
            'O(log(n))',
            'O(n)',
            'O(n^2)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          def factorial(n):
            if n <= 1:
              return 1
            return n * factorial(n - 1)
          
          What is the order of growth in big-O notation of factorial(n)?
          """
        },
        {
          'answer': '107a743d1908ef466c6b44d4b0f5325b',
          'choices': [
            '1',
            '2',
            '10',
            '100'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many total calls to factorial are made if we call factorial(10)?'
        },
        {
          'answer': '42a179bb94b9b0377d3a4f8a142db42a',
          'choices': [
            '1',
            '2',
            '100000',
            '10000000000'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          memo_dict = {}
          def factorial_memo(n):
            if n <= 1:
              return 1
            if n not in memo_dict:
              memo_dict[n] = n * factorial_memo(n - 1)
            return memo_dict[n]
          
          How many total calls to factorial_memo are made if we call factorial_memo(100000)?
          """
        },
        {
          'answer': '38636745428dd2c30958acf7c3ca16fc',
          'choices': [
            '1',
            '2',
            '100000',
            '10000000000'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many total calls to factorial_memo are made if we then call factorial_memo(100001)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
