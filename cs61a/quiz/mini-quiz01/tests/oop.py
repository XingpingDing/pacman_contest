test = {
  'name': 'OOP/Inheritance',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A(object):
          ...   x, y = 0, 0
          >>> class B(A):
          ...   pass
          >>> class C(A):
          ...   pass
          >>> print(A.x, B.x, C.x)
          590b571d9b9d5e30c1203c7f4897a3b8
          # locked
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          a725bdba334b78964100bfc8195719d9
          # locked
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          b33145896a96a390bfec8aa5df75e72a
          # locked
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          bff7eaaa5f35ce268936158c44355a05
          # locked
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          4c66dc5f84975a7575f753b66e7d38fb
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
