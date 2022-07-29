from main import check
import pytest


class TestFunc:
    
    @pytest.mark.parametrize(
        'staples, status',[
        ['(((([{}]))))', 'Balanced'],
        ['{{[()]}}', 'Balanced'],
        ['}{}', 'Unbalanced'],
        ['{{{}}}]', 'Unbalanced'],
    ]
    )
    def test_cls_check(self, staples, status):
        result = check(staples)
        assert result == status
    