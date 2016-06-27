test = {
  'name': 'Nonlocal',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> y = 4
          >>> def foo(x):
          ...     def bar():
          ...         nonlocal x, y
          ...         x = x + y
          ...         return x
          ...     return bar
          >>> # Remember for all WWPP questions, enter Error if it errors.
          >>> foo(3)()
          153d9c5833acfa1bc47de191aa8865bf
          # locked
          >>> def foo(x):
          ...     def bar(y):
          ...         nonlocal x, y
          ...         x = x + y
          ...         return x
          ...     return bar
          >>> foo(3)(4)
          153d9c5833acfa1bc47de191aa8865bf
          # locked
          >>> def foo(x):
          ...     def bar(y):
          ...         nonlocal x
          ...         x = x + y
          ...         return x
          ...     return bar
          >>> foo(3)(4)
          7cde72272c203b06e42fd5896752b484
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
